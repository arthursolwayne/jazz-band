
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),   # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Bass: Marcus, walking line in D, roots and fifths with chromatic approaches
# D2-G2 (MIDI 38-43), roots and fifths, chromatic approaches
# Bar 2: D2 (38), Eb2 (39), G2 (43), F#2 (42)
# Bar 3: A2 (45), Bb2 (46), D2 (38), C#2 (41)
# Bar 4: F#2 (42), G2 (43), A2 (45), Bb2 (46)

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F#2

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # C#2

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),  # Bb2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C#)
# Bar 3: Dm7 (D-F-A-C)
# Bar 4: Dmaj7 (D-F#-A-C#)
# Comp on 2 and 4

# Bar 2: 1.5 - 3.0s
piano_notes_bar2 = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # C#4
]

# Bar 3: 3.0 - 4.5s
piano_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # C4
]

# Bar 4: 4.5 - 6.0s
piano_notes_bar4 = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # C#4
]

for note in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Motif: D4 (62) - F#4 (67) - rest - A4 (71)
# Bar 2: Start the motif
# Bar 3: Let the rest breathe
# Bar 4: Resolve with A4

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # A4
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
