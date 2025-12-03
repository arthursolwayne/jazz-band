
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # A#2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A#2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # C#3
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),  # F#3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F#3
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # A#3
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # B3
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # D4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: Bm7 (B D F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # A5
])
# Bar 4: Gmaj7 (G B D F#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # F#5
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - B4 (a Dmaj7 arpeggio) with a slight delay on the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0625),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.4375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.8125),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=2.8125, end=3.0),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
