
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in
# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D2 (38), F (41), G2 (43), Bb (45), C (48), D2 (38), F (41), G2 (43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=52, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=55, start=1.5, end=1.875),  # C4
]

# Bar 3: Bb7 (Bb, D, F, Ab) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=110, pitch=47, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=110, pitch=49, start=2.25, end=2.625),  # Ab4
])

# Bar 4: Cm7 (C, Eb, G, Bb) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.375),  # Bb4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), Eb (63), F (64), rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
