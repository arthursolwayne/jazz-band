
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # E2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # Bb2 (root up a 5th)
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),  # A2 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # Bb2 (root)
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # C3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # C#3 (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),  # B2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - F7sus4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # F4 (root)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C5 (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # G4 (sus4)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E5 (extension),
    
    # Bar 3 (3.0 - 4.5s) - Bb7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb3 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F4 (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # D4 (flat 7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # A4 (extension),
    
    # Bar 4 (4.5 - 6.0s) - Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F4 (fifth)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb4 (minor 3rd)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # G4 (7th)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F - Bb - C - Bb (bars 2-4), with a slight delay in the third note
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F5
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # Bb5
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # C6
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.5),  # Bb5
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=110, pitch=76, start=3.25, end=3.5),  # Bb5
    pretty_midi.Note(velocity=110, pitch=77, start=3.5, end=3.75),  # C6
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.0),  # Bb5
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F5
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),  # Bb5
    pretty_midi.Note(velocity=110, pitch=77, start=5.0, end=5.25),  # C6
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),  # Bb5
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # F5
    pretty_midi.Note(velocity=110, pitch=68, start=5.75, end=6.0),  # D5 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
