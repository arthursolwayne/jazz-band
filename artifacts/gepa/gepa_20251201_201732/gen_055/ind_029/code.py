
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),   # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Marcus (Bass): Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F#2 (chromatic approach to G2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane (Piano): Open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D-G-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # C#5
]
piano.notes.extend(piano_notes)

# Dante (Sax): Melodic idea – one short motif, make it sing, leave it hanging
# D (62), F# (67), G (69), D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Marcus (Bass): Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F#2 (chromatic approach to G2)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane (Piano): Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),  # C5
]
piano.notes.extend(piano_notes)

# Dante (Sax): Melodic idea – continue motif with a variation
# D (62), F# (67), G (69), D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Marcus (Bass): Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F#2 (chromatic approach to G2)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane (Piano): Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # C#5
]
piano.notes.extend(piano_notes)

# Dante (Sax): Melodic idea – finish the motif with resolution
# D (62), F# (67), G (69), D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
