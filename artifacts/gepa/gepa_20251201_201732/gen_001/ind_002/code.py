
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F (D2), walking line with chromatic approaches
bass_notes = [
    # Bar 2, measure 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=2.125, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=2.5, end=2.875),  # A
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2, measure 1: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A
    # Bar 3, measure 2: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.5),  # D
    # Bar 4, measure 3: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2, measure 1: F (A4), G (B4), Bb (C5), F (A4)
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),  # F
    # Bar 3, measure 2: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),  # F
    # Bar 4, measure 3: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F (D2), walking line with chromatic approaches
bass_notes = [
    # Bar 3, measure 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=4.0, end=4.375),  # A
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3, measure 2: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
    # Bar 4, measure 3: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=76, start=3.625, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=4.0),  # G#
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=4.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    # Bar 3, measure 2: Continue motif
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5),  # F
    # Bar 4, measure 3: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F (D2), walking line with chromatic approaches
bass_notes = [
    # Bar 4, measure 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=5.125, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=5.5, end=5.875),  # A
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4, measure 3: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Finish motif
sax_notes = [
    # Bar 4, measure 3: Finish motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
