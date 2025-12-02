
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
# Bar 2
# Marcus on bass: F2 (D2-G2), root and fifth with chromatic approach
bass_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # F#2 chromatic
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # A2 (fifth of F)
]

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes_bar2 = [
    # Fmaj7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    # D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    # G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    # Fmaj7 (resolve)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),
]

# Bar 3
# Marcus on bass: F2, root and fifth with chromatic approach
bass_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
]

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes_bar3 = [
    # Bm7 (B D F# A)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    # C7 (C E G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),
    # Fmaj7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    # Fmaj7 (resolve)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),
]

# Bar 4
# Marcus on bass: F2, root and fifth with chromatic approach
bass_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
]

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes_bar4 = [
    # D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    # G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    # C7 (C E G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),
    # Fmaj7 (resolve)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
]

# Dante on sax: Motif in F, one short melody, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G4
]

for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes_bar2:
    bass.notes.append(note)
for note in bass_notes_bar3:
    bass.notes.append(note)
for note in bass_notes_bar4:
    bass.notes.append(note)

for note in piano_notes_bar2:
    piano.notes.append(note)
for note in piano_notes_bar3:
    piano.notes.append(note)
for note in piano_notes_bar4:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
