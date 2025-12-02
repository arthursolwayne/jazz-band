
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.tempo = 120  # 120 BPM

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125) for time in kick_times])
drums.notes.extend([pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125) for time in snare_times])
drums.notes.extend([pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125) for time in hihat_times])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # D#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G#
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=73, start=4.0, end=4.25),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),  # D
    # Bar 4 (continuation)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # D#
    pretty_midi.Note(velocity=100, pitch=77, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: C - E - B - D (C7 arpeggio)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
