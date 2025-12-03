
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Marcus - Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # C#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # F2 (chromatic approach)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.75), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5), # F2 (chromatic approach)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # C#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0), # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# PIANO: Diane - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # C5
    # Bar 3 (G7)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # F5
    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # B4
]
piano.notes.extend(piano_notes)

# SAX: Dante - Motif: G4 (1.5s), B4 (1.875s), D5 (2.25s), G4 (2.625s), leave hanging, return at 3.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4 (return)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0), # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5), # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
