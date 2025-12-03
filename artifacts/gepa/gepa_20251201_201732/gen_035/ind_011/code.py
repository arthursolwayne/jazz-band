
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38), F#2 (41), G2 (43), E2 (40)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),
    # Bar 3: G2 (43), Bb2 (42), C3 (48), A2 (45)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),
    # Bar 4: D2 (38), F#2 (41), G2 (43), E2 (40)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#) - open voicing
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C#4
    # Bar 3: G7 (G, B, D, F) - open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F4
    # Bar 4: Dm7 (D, F, A, C) - open voicing, resolving
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=6.0),   # E4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums continue for full 4 bars
# Bar 2: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
bar_2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),   # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),   # Snare
]
for note in bar_2_drum_notes:
    drums.notes.append(note)

# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
bar_3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),   # Snare
    pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),   # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.5),    # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75), # Snare
]
for note in bar_3_drum_notes:
    drums.notes.append(note)

# Bar 4: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
bar_4_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),   # Snare
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),   # Snare
]
for note in bar_4_drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
