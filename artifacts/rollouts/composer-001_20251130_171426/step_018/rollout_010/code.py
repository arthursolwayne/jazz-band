
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # G#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif that sings
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start+0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start+1.125, end=start+1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start+0.75, end=start+0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start+1.875, end=start+2.0)
# Hi-hat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start+0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start+0.375, end=start+0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start+0.75, end=start+1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start+1.125, end=start+1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start+1.5, end=start+1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start+1.875, end=start+2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start+2.25, end=start+2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start+2.625, end=start+3.0)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("wayne_intro.mid")
