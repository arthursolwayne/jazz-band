
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

kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 65),  # F
    (1.75, 66),  # Gb
    (2.0, 67),   # G
    (2.25, 69),  # A
    (2.5, 67),   # G
    (2.75, 65),  # F
    (3.0, 64),   # E
    (3.25, 62),  # D
    (3.5, 60),   # C
    (3.75, 62),  # D
    (4.0, 64),   # E
    (4.25, 65),  # F
    (4.5, 67),   # G
    (4.75, 69),  # A
    (5.0, 67),   # G
    (5.25, 65),  # F
    (5.5, 64),   # E
    (5.75, 62),  # D
]

for t, p in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 64),  # F7 (F, A, C, Eb)
    (2.0, 69),  # A
    (2.0, 60),  # C
    (2.0, 62),  # Eb
    (2.0, 64),  # F
    (4.0, 64),  # F7 again
    (4.0, 69),  # A
    (4.0, 60),  # C
    (4.0, 62),  # Eb
    (4.0, 64),  # F
]

for t, p in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.125)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66),  # G
    (1.75, 69),  # A
    (2.0, 67),  # G
    (2.25, 69),  # A
    (2.5, 67),  # G
    (2.75, 64),  # F
    (3.0, 66),  # G
    (3.25, 69),  # A
    (3.5, 67),  # G
    (3.75, 69),  # A
    (4.0, 67),  # G
    (4.25, 64),  # F
    (4.5, 66),  # G
    (4.75, 69),  # A
    (5.0, 67),  # G
    (5.25, 69),  # A
    (5.5, 67),  # G
    (5.75, 64),  # F
]

for t, p in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=p, start=t, end=t + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
