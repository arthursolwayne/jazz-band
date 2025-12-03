
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2 (root)
    
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125), # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2 (root)
    
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Fm7 (F, Ab, C, D)
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D
    
    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # G
    
    # Bar 4 (Gm7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing
# Motif: F - Ab - Bb - D (Fm7 arpeggio with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # D
    
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # D
    
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
