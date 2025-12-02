
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> C#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.25),
    # Bar 3: A2 (fifth) -> G#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    # Bar 4: D2 (root) -> C#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # C#5
]
# Bar 3: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # A5
])
# Bar 4: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # G4 (D in root position)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # F4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> E4 (64) -> D4 (62) -> C#4 (61)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
]
# Bar 3: Leave it hanging (no note)
# Bar 4: Come back and finish
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C#4
])
sax.notes.extend(sax_notes)

# Drums for Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.3125, end=start_time + 1.5),
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.3125, end=start_time + 1.5),
    ]
    drums.notes.extend(drum_notes)

# Add drums for Bar 2
add_drums(1.5)
# Add drums for Bar 3
add_drums(2.25)
# Add drums for Bar 4
add_drums(3.0)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
