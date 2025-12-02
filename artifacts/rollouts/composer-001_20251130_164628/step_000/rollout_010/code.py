
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
bar_length = 1.5
for i in range(4):
    kick_time = i * bar_length + 0.0
    snare_time = i * bar_length + 0.75
    hihat_time = i * bar_length + 0.125
    for j in range(8):
        hihat_time = i * bar_length + j * 0.125
        note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: Fm7, Ab7, Bb7, C7
bass_notes = [
    (1.5, 53),     # F (Fm7)
    (1.75, 51),    # Eb
    (2.0, 50),     # D
    (2.25, 53),    # F
    (2.5, 55),     # G
    (2.75, 53),    # F
    (3.0, 51),     # Eb
    (3.25, 50),    # D
    (3.5, 53),     # F (Ab7)
    (3.75, 51),    # Eb
    (4.0, 48),     # C
    (4.25, 53),    # F
    (4.5, 55),     # G
    (4.75, 53),    # F
    (5.0, 51),     # Eb
    (5.25, 50),    # D
    (5.5, 53),     # F (Bb7)
    (5.75, 51),    # Eb
    (6.0, 52),     # Db
    (6.25, 53),    # F
    (6.5, 55),     # G
    (6.75, 53),    # F
    (7.0, 51),     # Eb
    (7.25, 50),    # D
    (7.5, 53),     # F (C7)
    (7.75, 51),    # Eb
    (8.0, 52),     # Db
    (8.25, 53),    # F
    (8.5, 55),     # G
    (8.75, 53),    # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 53, 1.5),   # F7
    (1.5, 60, 1.5),   # A
    (1.5, 64, 1.5),   # C
    (1.5, 67, 1.5),   # Eb
    (2.0, 53, 1.5),   # F7
    (2.0, 60, 1.5),   # A
    (2.0, 64, 1.5),   # C
    (2.0, 67, 1.5),   # Eb
    (2.5, 53, 1.5),   # Ab7
    (2.5, 61, 1.5),   # Bb
    (2.5, 64, 1.5),   # C
    (2.5, 67, 1.5),   # Eb
    (3.0, 53, 1.5),   # Bb7
    (3.0, 62, 1.5),   # B
    (3.0, 64, 1.5),   # C
    (3.0, 67, 1.5),   # Eb
    (3.5, 53, 1.5),   # C7
    (3.5, 60, 1.5),   # A
    (3.5, 64, 1.5),   # C
    (3.5, 67, 1.5),   # Eb
    (4.0, 53, 1.5),   # F7
    (4.0, 60, 1.5),   # A
    (4.0, 64, 1.5),   # C
    (4.0, 67, 1.5),   # Eb
    (4.5, 53, 1.5),   # Ab7
    (4.5, 61, 1.5),   # Bb
    (4.5, 64, 1.5),   # C
    (4.5, 67, 1.5),   # Eb
    (5.0, 53, 1.5),   # Bb7
    (5.0, 62, 1.5),   # B
    (5.0, 64, 1.5),   # C
    (5.0, 67, 1.5),   # Eb
    (5.5, 53, 1.5),   # C7
    (5.5, 60, 1.5),   # A
    (5.5, 64, 1.5),   # C
    (5.5, 67, 1.5),   # Eb
    (6.0, 53, 1.5),   # F7
    (6.0, 60, 1.5),   # A
    (6.0, 64, 1.5),   # C
    (6.0, 67, 1.5),   # Eb
    (6.5, 53, 1.5),   # Ab7
    (6.5, 61, 1.5),   # Bb
    (6.5, 64, 1.5),   # C
    (6.5, 67, 1.5),   # Eb
    (7.0, 53, 1.5),   # Bb7
    (7.0, 62, 1.5),   # B
    (7.0, 64, 1.5),   # C
    (7.0, 67, 1.5),   # Eb
    (7.5, 53, 1.5),   # C7
    (7.5, 60, 1.5),   # A
    (7.5, 64, 1.5),   # C
    (7.5, 67, 1.5),   # Eb
]
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 0.375),  # G
    (1.875, 64, 0.375),  # C
    (2.25, 62, 0.375),  # G
    (2.625, 64, 0.375),  # C
    (3.0, 62, 0.375),   # G
    (3.375, 65, 0.375),  # D
    (3.75, 62, 0.375),  # G
    (4.125, 64, 0.375),  # C
    (4.5, 62, 0.375),   # G
    (4.875, 64, 0.375),  # C
    (5.25, 62, 0.375),  # G
    (5.625, 65, 0.375),  # D
    (6.0, 62, 0.375),   # G
    (6.375, 64, 0.375),  # C
    (6.75, 62, 0.375),  # G
    (7.125, 64, 0.375),  # C
    (7.5, 62, 0.375),   # G
    (7.875, 65, 0.375),  # D
    (8.25, 62, 0.375),  # G
    (8.625, 64, 0.375),  # C
    (9.0, 62, 0.375),   # G
    (9.375, 65, 0.375),  # D
    (9.75, 62, 0.375),  # G
    (10.125, 64, 0.375),  # C
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo.mid")
