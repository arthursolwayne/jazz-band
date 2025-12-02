
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
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS LINE - Marcus
# Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 42),  # F
    (1.75, 43),  # Gb
    (2.0, 40),  # Eb
    (2.25, 39),  # D
    (2.5, 38),  # C
    (2.75, 37),  # Bb
    (3.0, 36),  # A
    (3.25, 40),  # Eb
    (3.5, 42),  # F
    (3.75, 43),  # Gb
    (4.0, 39),  # D
    (4.25, 38),  # C
    (4.5, 37),  # Bb
    (4.75, 40),  # Eb
    (5.0, 42),  # F
    (5.25, 44),  # G
    (5.5, 41),  # E
    (5.75, 42),  # F
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# PIANO - Diane
# 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# Am7 = A, C, E, G
piano_notes = [
    # Bar 2
    (2.0, 71),  # F
    (2.0, 67),  # Ab
    (2.0, 69),  # C
    (2.0, 64),  # Eb
    # Bar 3
    (3.0, 74),  # Bb
    (3.0, 72),  # D
    (3.0, 71),  # F
    (3.0, 67),  # Ab
    # Bar 4
    (4.0, 69),  # Eb
    (4.0, 71),  # G
    (4.0, 74),  # Bb
    (4.0, 66),  # Db
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# SAX - Dante
# Motif: F, Eb, G, F (with some chromaticism)
sax_notes = [
    (2.0, 71),  # F
    (2.25, 69),  # Eb
    (2.5, 72),  # G
    (2.75, 71),  # F
    (3.0, 71),  # F
    (3.25, 69),  # Eb
    (3.5, 72),  # G
    (3.75, 71),  # F
    (4.0, 71),  # F
    (4.25, 69),  # Eb
    (4.5, 72),  # G
    (4.75, 71),  # F
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
