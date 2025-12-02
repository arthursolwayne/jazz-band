
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),   # A (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),   # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),  # G2 (root)
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75), # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=75, start=3.75, end=4.125), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # G2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),   # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=4.875),  # A2 (root)
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25), # B2 (fifth)
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.625), # A#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=77, start=5.625, end=6.0),  # A2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Different chord each bar, resolve on the last
# Bar 4: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=79, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=79, start=5.75, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
