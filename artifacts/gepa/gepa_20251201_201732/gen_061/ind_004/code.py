
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

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # C#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625), # F#3
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875), # C#4
]
# Bar 3: Bm7 (B D F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # A4
])
# Bar 4: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # A4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # C4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - B4 - D4 (1st bar), then D4 - F#4 - B4 (2nd bar), then D4 (3rd bar), then D4 (4th bar)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4 (end of first motif)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Drums: continue with hihat on every eighth, kick on 1 and 3, snare on 2 and 4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on &2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on &4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on &2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on &4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on &2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on &4
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.75), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
