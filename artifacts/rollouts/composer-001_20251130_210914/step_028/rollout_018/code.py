
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Fm bass line: F, Eb, D, C, Bb, A, G, F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 on 1 and 3, Bbm7 on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875), # C
    # Bar 2: Bbm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F
    # Bar 3: Fm7 on beat 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75), # C
    # Bar 3: Bbm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5), # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5), # F
    # Bar 4: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875), # C
    # Bar 4: Bbm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_piece.mid")
