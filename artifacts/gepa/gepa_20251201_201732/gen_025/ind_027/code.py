
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the quartet
# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)  # D
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)  # F#
note3 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)  # A
note4 = pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0)  # C#
piano.notes.extend([note1, note2, note3, note4])

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 -> E2 -> F#2 -> G2
note1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # D
note2 = pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)  # E
note3 = pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625)  # F#
note4 = pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0)  # G
bass.notes.extend([note1, note2, note3, note4])

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Bb - D - Bb (MIDI 60 - 65 - 60)
note1 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)  # D
sax.notes.extend([note1, note2])

# Bar 3: Diane: Gm7 (G Bb D F)
note1 = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5)  # G
note2 = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5)  # Bb
note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5)  # D
note4 = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5)  # F
piano.notes.extend([note1, note2, note3, note4])

# Marcus: Walking bass line (G2 -> A2 -> B2 -> C2)
note1 = pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375)  # G
note2 = pretty_midi.Note(velocity=100, pitch=45, start=2.375, end=2.75)  # A
note3 = pretty_midi.Note(velocity=100, pitch=47, start=2.75, end=3.125)  # B
note4 = pretty_midi.Note(velocity=100, pitch=49, start=3.125, end=3.5)  # C
bass.notes.extend([note1, note2, note3, note4])

# Dante: Tenor sax — continue the motif, resolve it
note1 = pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5)  # D
note3 = pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75)  # Bb
note4 = pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0)  # D
sax.notes.extend([note1, note2, note3, note4])

# Bar 4: Diane: Cmaj7 (C E G B)
note1 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5)  # C
note2 = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5)  # E
note3 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5)  # G
note4 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5)  # B
piano.notes.extend([note1, note2, note3, note4])

# Marcus: Walking bass line (C2 -> D2 -> E2 -> F2)
note1 = pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375)  # C
note2 = pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75)  # D
note3 = pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125)  # E
note4 = pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5)  # F
bass.notes.extend([note1, note2, note3, note4])

# Dante: Tenor sax — finish the motif, leave it hanging
note1 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5)  # D
sax.notes.extend([note1, note2])

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
# midi.write disabled
