
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: F2 (MIDI 53) -> C2 (MIDI 48) -> Gb2 (MIDI 50) -> Bb2 (MIDI 52)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25),  # C2 on 2
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Gb2 on 3
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # Bb2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Fm7 -> Am7 -> Cm7 -> Eb7
# Open voicings, resolve on the last
piano_notes = [
    # Fm7: F, Ab, C, Eb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Eb
    # Am7: A, C, E, G
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # G
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Bb
    # Eb7: Eb, G, Bb, D
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    bar_start = 1.5 + i * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing
# F (66), Ab (65), Bb (67), F (66)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.65, end=1.8),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.8, end=1.95),   # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=1.95, end=2.1),   # F
    # Repeat the motif after a rest, leaving it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=2.4, end=2.55),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.55, end=2.7),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.7, end=2.85),   # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.85, end=3.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
