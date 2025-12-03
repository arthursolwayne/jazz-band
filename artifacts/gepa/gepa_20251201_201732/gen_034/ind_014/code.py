
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F#2 (chromatic approach)
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # E2 (chromatic approach)
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    
    # Bar 4: C#m7 (C#, E, G, B)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875), # F#5
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # F#5
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # D5
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
