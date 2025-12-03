
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus - Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # A2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=3.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # A2
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.25),  # A2
    pretty_midi.Note(velocity=90, pitch=40, start=4.25, end=4.5),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.75, end=5.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # A2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=5.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=6.0),  # F#2
]
bass.notes.extend(bass_notes)

# Diane - Piano, open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # C#4
]
# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # F#4
])
# Bar 4: A7 (A, C#, E, G#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0),  # C#4
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0),  # E4
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),  # G#4
])
# Bar 2: D7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.5),  # D3
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.5),  # F#3
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.5),  # A3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.5),  # C#3
])
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=4.0),  # G3
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=4.0),  # B3
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=4.0),  # D3
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=4.0),  # F#3
])
# Bar 4: A7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=63, start=4.0, end=4.5),  # A3
    pretty_midi.Note(velocity=90, pitch=57, start=4.0, end=4.5),  # C#3
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.5),  # E3
    pretty_midi.Note(velocity=90, pitch=63, start=4.0, end=4.5),  # G#3
])
piano.notes.extend(piano_notes)

# Dante - Tenor sax, short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.25),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare, hihat])

# Add drum fills between bars
for bar in range(2, 5):
    start = bar * 1.5
    fill = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5)
    fill2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.875, end=start + 1.0)
    fill3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.25, end=start + 1.375)
    drums.notes.extend([fill, fill2, fill3])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
