
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0.0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62), (1.75, 64), (2.0, 65), (2.25, 67),
    (2.5, 69), (2.75, 71), (3.0, 72), (3.25, 74),
    (3.5, 76), (3.75, 77), (4.0, 79), (4.25, 81),
    (4.5, 83), (4.75, 84), (5.0, 86), (5.25, 88)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 71),
    (2.0, 60), (2.0, 64), (2.0, 67), (2.0, 71),
    (2.5, 60), (2.5, 64), (2.5, 67), (2.5, 71),
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 71),
    (3.5, 60), (3.5, 64), (3.5, 67), (3.5, 71),
    (4.0, 60), (4.0, 64), (4.0, 67), (4.0, 71),
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71),
    (5.0, 60), (5.0, 64), (5.0, 67), (5.0, 71)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
            drums.notes.append(note)

# Sax: Motif (C E G) on beat 1, then leave it hanging
sax_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67),
    (2.0, 67)  # Hold the G for a bit
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.5)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_moment.mid")
