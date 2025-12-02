
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # G7
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G7
]
piano.notes.extend(piano_notes)

# Sax (Dante): Whisper to cry. A short motif with space and emotion
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),    # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),    # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),    # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),    # C
    pretty_midi.Note(velocity=95, pitch=65, start=2.75, end=3.0),    # E (higher energy)
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),    # G
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),    # D
    pretty_midi.Note(velocity=95, pitch=62, start=3.5, end=3.75),    # C
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.0),    # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.0, end=4.25),    # G
    pretty_midi.Note(velocity=95, pitch=65, start=4.25, end=4.5),    # E
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),    # D
    pretty_midi.Note(velocity=95, pitch=62, start=4.75, end=5.0),    # C
    pretty_midi.Note(velocity=95, pitch=65, start=5.0, end=5.25),    # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # G (peak)
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    bar_start = 1.5 + (bar - 1) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Hihat on 1
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 2
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    # Kick on 3
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on 3
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    # Snare on 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on 4
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.6875)
    drums.notes.extend([kick, hihat, snare, hihat2, kick2, hihat3, snare2, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
