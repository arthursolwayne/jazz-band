
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625), # C#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0), # F#2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375), # F#2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # C#3 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5), # F#3 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875), # F#3
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # C#4 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # B3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0), # F#4 (chromatic approach)
]

bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # C#5
]

# Bar 3: G7 (G-B-D-F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F#5
])

# Bar 4: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # A5
])

# Bar 4 resolution: D7 (D-F#-A-C#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # C#5
])

piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - D5 (16th notes)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625), # A4
    pretty_midi.Note(velocity=110, pitch=72, start=2.0625, end=2.25), # D5
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875), # D4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625), # A4
    pretty_midi.Note(velocity=110, pitch=72, start=3.5625, end=3.75), # D5
]

sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # Kick on 3
])

# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
])

# Bar 4 (4.5 - 6.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
