
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # C#
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0)   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # G
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),   # G
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),   # G
]
piano.notes.extend(piano_notes)

# Sax: Melody with rests and emotional resonance
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),    # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),    # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),    # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),    # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),    # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),    # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.125, end=5.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),    # Bb
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375))  # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)) # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)) # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))  # Snare on 4
    # Hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
