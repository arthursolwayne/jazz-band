
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (41) on 2 (approach to G2)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),
    # G2 (43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # B2 (46) on 4 (approach to C#3)
    pretty_midi.Note(velocity=90, pitch=46, start=2.375, end=2.625),
    # C#3 (47) on 1
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=2.875),
    # D2 (38) on 2
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C5
]

# Bar 3: Gmaj7 (G-B-D-F#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),  # F#5
])

# Bar 4: C minor (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=2.875, end=3.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),  # Bb4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (62), F#4 (67), G4 (67), D4 (62) — short motif with a slight tension on F# and then resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=2.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),   # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.375), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.875), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),   # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
