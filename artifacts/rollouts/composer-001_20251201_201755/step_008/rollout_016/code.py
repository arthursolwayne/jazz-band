
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the melody
# Sax: motif starting on D (62), with a chromatic descent to C# (61), then resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D (D2=38), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375), # G2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # A2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875), # Bb2 (root)
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # D3 (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875), # F#
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875), # C#
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=95, pitch=76, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625), # F
])
# Bar 4: Cmaj7 (C-E-G-B)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375), # B
])
# Bar 4 resolution: Dmaj7 again
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875), # C#
])
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
