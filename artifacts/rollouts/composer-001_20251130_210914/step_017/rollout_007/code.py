
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet

# Bass line: walking line with chromatic approaches, never the same note twice
# D minor: D, F, G, A, Bb, C, Db
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),  # Db
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D minor 7: D, F, A, C
# Chord on 2 and 4, root motion: D -> Bb -> D
chord2 = [62, 64, 67, 69]  # Dm7
chord4 = [66, 68, 61, 64]  # Bb7
# Bar 2, beat 2
for note in chord2:
    pretty_midi.Note(velocity=90, pitch=note, start=2.25, end=2.625)
# Bar 3, beat 2
for note in chord4:
    pretty_midi.Note(velocity=90, pitch=note, start=3.75, end=4.125)
# Bar 4, beat 2
for note in chord2:
    pretty_midi.Note(velocity=90, pitch=note, start=5.25, end=5.625)
piano.notes.extend([pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
                    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
                    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
                    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
                    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),  # Bb
                    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0),  # Db
                    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0),  # B
                    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
                    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
                    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
                    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
                    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # C
                    ])

# Saxophone: One short motif, make it sing — D, Eb, E, D (brief, leaving it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),   # D
    pretty_midi.Note(velocity=110, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
