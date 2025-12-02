
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
bar_1_start = 0.0
bar_1_end = 1.5

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start, end=bar_1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start + 0.75, end=bar_1_start + 1.125))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 0.375, end=bar_1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 1.125, end=bar_1_start + 1.5))

# Hihat
for i in range(4):
    hihat_start = bar_1_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
# Fm: F, Ab, Bb, D, Eb
# Walking bass line with chromatic passing tones

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=61, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, Bb, Db
# Cm7 = C, Eb, F, G
# Gm7 = G, Bb, C, D
# Dm7 = D, F, G, A
# 2nd and 4th beats

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25))  # Ab
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.25))  # Db

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75))  # Eb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75))  # G

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25))  # D

# Sax: Motif (1.5 - 3.0s)
# Fm: F, Ab, Bb, C, Eb
# Motif: F, Ab, Bb, then a hold on Eb

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),   # Eb
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    bar_end = bar_start + 1.5

    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))

    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))

    # Hihat on every eighth
    for i in range(4):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
