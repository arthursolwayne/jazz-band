
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # Snare on 4 (but ends at 1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: D2 (38) to G2 (43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A5
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875), # C6
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875), # E6
]

# Bar 3: Dm7 (D, F, A, C)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # A4
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375), # C5
]

# Bar 4: G7 (G, B, D, F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875), # G5
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875), # B5
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.875), # D6
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875), # F5
]
piano.notes.extend(piano_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)  # Snare on 4
]
drums.notes.extend(drum_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (72) to A (76) to Bb (77) to A (76) — a question, a challenge, a memory
# Bar 2: Start motif (F, A, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25), # A5
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.625), # Bb5
    # Leave it hanging
    # Bar 3: Nothing
    # Bar 4: Come back and finish with A (76)
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.875),  # A5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
