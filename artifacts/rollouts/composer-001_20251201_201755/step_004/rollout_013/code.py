
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F (root)
    
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # Db (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # C (fifth)
    
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25), # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),  # Ab (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: Diane (open voicings, resolve on last beat)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875),  # Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=57, start=2.25, end=2.625),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),
    
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.375),  # Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),
    
    # Bar 3 (second half)
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75),
    
    # Bar 4 (second half)
    pretty_midi.Note(velocity=95, pitch=60, start=4.125, end=4.5),   # Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=71, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Tenor Sax: Dante (motif, make it sing)
# Motif: F - Bb - G - F
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F
    
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_russo_4bar.mid')
