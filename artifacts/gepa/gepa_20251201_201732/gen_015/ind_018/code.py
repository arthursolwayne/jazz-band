
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
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start, end=bar1_start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.5, end=bar1_start + 1.6875),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # C3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D2

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # C5
]

# Bar 3: Gm7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=75, start=3.0, end=3.5),  # F5
])

# Bar 4: Cm7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0),  # Bb4
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start the motif on beat 1 of bar 2 (1.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),   # F4
    # Leave it hanging (end of bar 2 at 2.0s), come back at the start of bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F4
    # End the motif at the start of bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue for the full 6 seconds
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

def add_drums(start):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.6875),
    for note in drum_notes:
        drums.notes.append(note)

# Bar 2
add_drums(bar2_start)
# Bar 3
add_drums(bar3_start)
# Bar 4
add_drums(bar4_start)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
