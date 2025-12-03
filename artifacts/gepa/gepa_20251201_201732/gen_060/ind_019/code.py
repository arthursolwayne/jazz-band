
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # Snare on 4 (but we're only going to 1.5s)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass - Marcus: walking line, roots and fifths, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0), # D2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375), # A2
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875), # Ab2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2
]
bass.notes.extend(bass_notes)

# Piano - Diane: open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C#4
]

# Bar 3: Bm7 (B, D, F#, A)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # A4
]

# Bar 4: G7 (G, B, D, F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F4
]

# Resolve on the last chord (G7)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F4
]
piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - B4 - D4 (Dmaj7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75), # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875), # B4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0), # D4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75), # D4 (come back)
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875), # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0), # B4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125), # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass - Bar 3: Bm7 (B, D, F#, A)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375), # B2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5), # B2
]
bass.notes.extend(bass_notes)

# Bass - Bar 4: G7 (G, B, D, F)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875), # G3
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # B3 (fifth)
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # A3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0), # G3
]
bass.notes.extend(bass_notes)

# Sax - Bar 3: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25), # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375), # B4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5), # D4
]
sax.notes.extend(sax_notes)

# Sax - Bar 4: Play the motif again, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75), # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=4.875), # B4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0), # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
