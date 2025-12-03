
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (MIDI 41) on 2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # B2 (MIDI 46) on 4 (fifth of D)
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0)   # C#4
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.125),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.5),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.875)   # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # B2 (MIDI 46) on 2 (fifth of D)
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.625),
    # D2 (MIDI 38) on 3
    pretty_midi.Note(velocity=90, pitch=38, start=3.625, end=4.0),
    # F#2 (MIDI 41) on 4 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=41, start=4.0, end=4.375)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5)   # C4
]
piano.notes.extend(piano_notes)

# Sax: Motif - continue and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5)   # C#5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C#2 (MIDI 40) on 1 (chromatic approach to D2)
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),
    # D2 (MIDI 38) on 2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.125),
    # F#2 (MIDI 41) on 3 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=41, start=5.125, end=5.5),
    # G2 (MIDI 43) on 4
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)   # C#4
]
piano.notes.extend(piano_notes)

# Sax: Motif - finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # B4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # C#5
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0)   # B4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
