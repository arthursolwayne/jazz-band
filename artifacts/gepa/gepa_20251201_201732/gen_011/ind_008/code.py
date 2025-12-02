
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
# Bar 2: D (MIDI 38), F# (MIDI 42), G (MIDI 43), D (MIDI 38)
bass_notes_bar2 = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
]
# Bar 3: A (MIDI 45), C# (MIDI 49), D (MIDI 50), A (MIDI 45)
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),
]
# Bar 4: D (MIDI 38), F# (MIDI 42), G (MIDI 43), D (MIDI 38)
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes_bar2 + bass_notes_bar3 + bass_notes_bar4)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Dmaj7 (D, F#, A, C#) MIDI 38, 42, 50, 55
piano_notes_bar2 = [
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=2.25),  # D
]
# Bar 3: Amaj7 (A, C#, E, G#) MIDI 45, 49, 57, 62
piano_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.75),
]
# Bar 4: D7 (D, F#, A, C) MIDI 38, 42, 50, 52
piano_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=5.25),
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif (D, F#, A)
sax_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.4375),
]
# Bar 4: Finish the motif (D, F#, A)
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.4375),
]
sax.notes.extend(sax_notes_bar2 + sax_notes_bar4)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
# Bar 3 (3.0 - 4.5)
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
# Bar 4 (4.5 - 6.0)
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
# Add hihat on every eighth
for i in range(1.5, 6.0, 0.375):
    pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375)
    if i + 0.375 <= 6.0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375))

drums.notes.extend(drum_notes_bar2 + drum_notes_bar3 + drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
