
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0), # D2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5), # G2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0), # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2 (1.5 - 3.0s): D7sus4 (D, G, C#, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0), # B4
]

# Bar 3 (3.0 - 4.5s): Bm7b5 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # A4
])

# Bar 4 (4.5 - 6.0s): G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0), # F#4
])

piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875), # Hihat
]

# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375), # Hihat
])

# Bar 4 (4.5 - 6.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.5),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875), # Hihat
])

drums.notes.extend(drum_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F#4, G4, D5 (start on bar 2, mid-bar 2, end on bar 3)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D5
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_moment.mid")
