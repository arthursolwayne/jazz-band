
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # A (fifth)
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # F (root)
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),   # C (root of next chord)
    pretty_midi.Note(velocity=80, pitch=78, start=3.375, end=3.75),  # E (fifth)
    pretty_midi.Note(velocity=80, pitch=75, start=3.75, end=4.125),  # D# (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),   # C (root)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),   # A (fifth)
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # F (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # A (fifth)
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),   # F (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # E
]
# Bar 3: Dm7 (D F A C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # C
])
# Bar 4: C7 (C E G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),   # C
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - A - Bb - C (F A Bb C), then repeat with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
