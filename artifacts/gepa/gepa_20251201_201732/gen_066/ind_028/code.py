
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
# Bar 2: D (MIDI 38) -> F# (MIDI 42)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # F# (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D (root)
]
bass.notes.extend(bass_notes)

# Bar 3: Bm7 (MIDI 40-45)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # B (root)
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125), # F# (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # B (root)
]
bass.notes.extend(bass_notes)

# Bar 4: G7 (MIDI 43-47)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G (root)
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25), # B (chromatic)
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.625), # D (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # G (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Dmaj7 (MIDI 42, 46, 50, 52)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.75),  # C#
]
piano.notes.extend(piano_notes)

# Bar 3: Bm7 (MIDI 40, 44, 47, 52)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # A
]
piano.notes.extend(piano_notes)

# Bar 4: G7 (MIDI 43, 47, 50, 52)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.75),  # F#
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Bar 2: Motif starts (D, F#, A)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
]
sax.notes.extend(sax_notes)

# Bar 4: Finish the motif (C#, D, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
