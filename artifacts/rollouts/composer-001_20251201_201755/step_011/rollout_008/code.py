
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # Ab
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),   # Bb
]

for note in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(note)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm triad with a tritone)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=59, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),  # F (resolve on beat 2)
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=4.125), # F (come back later)
    pretty_midi.Note(velocity=110, pitch=61, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=59, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25), # F (finish it)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('waynes_moment.mid')
