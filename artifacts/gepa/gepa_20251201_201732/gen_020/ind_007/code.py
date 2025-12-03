
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=80, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=80, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=80, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bar 2: Full band (1.5 - 3.0s)
start = 1.5
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=start, end=start + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=start + 0.375, end=start + 0.75),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=start + 0.75, end=start + 1.125),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=start, end=start + 0.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: Start the motif (D, F#, A)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=start + 0.75, end=start + 1.125),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full band (3.0 - 4.5s)
start = 3.0
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=start, end=start + 0.375),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=start + 0.375, end=start + 0.75),  # B2
    pretty_midi.Note(velocity=80, pitch=38, start=start + 0.75, end=start + 1.125),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=start + 1.125, end=start + 1.5),  # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Cmaj7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=start, end=start + 0.375),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=start, end=start + 0.375),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=start + 0.75, end=start + 1.125),  # A4
]
sax.notes.extend(sax_notes)

# Bar 4: Full band (4.5 - 6.0s)
start = 4.5
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=start, end=start + 0.375),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=start + 0.375, end=start + 0.75),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=start + 0.75, end=start + 1.125),  # B2
    pretty_midi.Note(velocity=80, pitch=47, start=start + 1.125, end=start + 1.5),  # C#3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),  # A4
    pretty_midi.Note(velocity=90, pitch=66, start=start, end=start + 0.375),  # F#4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif (D, F#, A, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=start + 0.75, end=start + 1.125),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums: same pattern as bar 1
for bar in range(1):
    start = 4.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=80, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=80, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=80, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
