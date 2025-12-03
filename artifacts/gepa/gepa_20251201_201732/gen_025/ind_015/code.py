
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # G2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E
]

# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # F
])

# Bar 4: F7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # F
])

# Bar 4: C7 (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # B
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - G - F (MIDI 57 - 50 - 60 - 57)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # F (return)
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue with fills and rhythm
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
