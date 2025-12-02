
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 48, 100), # Fm7
    (1.875, 49, 100), # Gb
    (2.25, 50, 100), # Ab
    (2.625, 48, 100), # F
    # Bar 3
    (3.0, 51, 100), # Bb
    (3.375, 50, 100), # Ab
    (3.75, 49, 100), # Gb
    (4.125, 48, 100), # F
    # Bar 4
    (4.5, 51, 100), # Bb
    (4.875, 50, 100), # Ab
    (5.25, 49, 100), # Gb
    (5.625, 48, 100) # F
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62, 100), # E7
    (1.875, 60, 100), # G
    (1.875, 58, 100), # Bb
    (1.875, 55, 100), # D
    (2.625, 62, 100), # E7
    (2.625, 60, 100), # G
    (2.625, 58, 100), # Bb
    (2.625, 55, 100), # D
    # Bar 3
    (3.375, 62, 100), # E7
    (3.375, 60, 100), # G
    (3.375, 58, 100), # Bb
    (3.375, 55, 100), # D
    (4.125, 62, 100), # E7
    (4.125, 60, 100), # G
    (4.125, 58, 100), # Bb
    (4.125, 55, 100), # D
    # Bar 4
    (4.875, 62, 100), # E7
    (4.875, 60, 100), # G
    (4.875, 58, 100), # Bb
    (4.875, 55, 100), # D
    (5.625, 62, 100), # E7
    (5.625, 60, 100), # G
    (5.625, 58, 100), # Bb
    (5.625, 55, 100), # D
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    for beat in range(4):
        time = bar_start + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Dante: Tenor sax — one short motif, make it sing
# Start on F, then Bb, then Gb, then F again
sax_notes = [
    (1.5, 64, 110), # F
    (1.875, 60, 110), # Bb
    (2.25, 61, 110), # Gb
    (2.625, 64, 110), # F
    (3.0, 64, 110), # F (repeat)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
