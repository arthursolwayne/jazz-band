
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    kick_notes = [36]
    snare_notes = [38]
    hihat_notes = [42]
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 48, 100), (1.75, 49, 100), (2.0, 50, 100), (2.25, 51, 100),
    (2.5, 52, 100), (2.75, 51, 100), (3.0, 50, 100), (3.25, 49, 100),
    (3.5, 51, 100), (3.75, 52, 100), (4.0, 53, 100), (4.25, 51, 100),
    (4.5, 50, 100), (4.75, 49, 100), (5.0, 51, 100), (5.25, 52, 100),
    (5.5, 53, 100), (5.75, 51, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60, 100), (1.5, 64, 100), (1.5, 67, 100), (1.5, 71, 100),  # F7
    (2.0, 62, 100), (2.0, 66, 100), (2.0, 69, 100), (2.0, 72, 100),  # A7
    (2.5, 60, 100), (2.5, 64, 100), (2.5, 67, 100), (2.5, 71, 100),  # F7
    (3.0, 62, 100), (3.0, 66, 100), (3.0, 69, 100), (3.0, 72, 100),  # A7
    (3.5, 60, 100), (3.5, 64, 100), (3.5, 67, 100), (3.5, 71, 100),  # F7
    (4.0, 62, 100), (4.0, 66, 100), (4.0, 69, 100), (4.0, 72, 100),  # A7
    (4.5, 60, 100), (4.5, 64, 100), (4.5, 67, 100), (4.5, 71, 100),  # F7
    (5.0, 62, 100), (5.0, 66, 100), (5.0, 69, 100), (5.0, 72, 100)   # A7
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2, 3]:
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65, 100), (1.525, 67, 100), (1.55, 64, 100), (1.575, 62, 100),
    (2.0, 65, 100), (2.025, 67, 100), (2.05, 64, 100), (2.075, 62, 100),
    (2.5, 65, 100), (2.525, 67, 100), (2.55, 64, 100), (2.575, 62, 100),
    (3.0, 65, 100), (3.025, 67, 100), (3.05, 64, 100), (3.075, 62, 100),
    (3.5, 65, 100), (3.525, 67, 100), (3.55, 64, 100), (3.575, 62, 100),
    (4.0, 65, 100), (4.025, 67, 100), (4.05, 64, 100), (4.075, 62, 100),
    (4.5, 65, 100), (4.525, 67, 100), (4.55, 64, 100), (4.575, 62, 100),
    (5.0, 65, 100), (5.025, 67, 100), (5.05, 64, 100), (5.075, 62, 100)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.05)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
