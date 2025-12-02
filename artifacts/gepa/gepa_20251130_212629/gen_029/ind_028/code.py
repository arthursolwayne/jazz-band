
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Hihat on every eighth, kick on 1 and 3, snare on 2 and 4, but with variation
# Create tension with slight timing shifts and dynamic variation

drum_kick_1 = pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375)
drum_snare_1 = pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125)
drum_hihat_1 = pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5)

drum_kick_2 = pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5)
drum_snare_2 = pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875)  # Slight syncopation
drum_hihat_2 = pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=2.0)

drums.notes.extend([drum_kick_1, drum_snare_1, drum_hihat_1, drum_kick_2, drum_snare_2, drum_hihat_2])

# Bar 2-4: Full Quartet (1.5s - 6.0s)

# Bass line: Marcus
# Walking line, chromatic approaches, never the same note twice
# F7 voicing: F, A, C, E (but he’s walking, not just comping)

bass_notes = [
    pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.875),  # F (3rd octave)
    pretty_midi.Note(velocity=75, pitch=69, start=1.875, end=2.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=75, pitch=73, start=2.625, end=3.0),  # G (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=75, pitch=69, start=3.375, end=3.75),  # E (Approach)
    pretty_midi.Note(velocity=70, pitch=71, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=75, pitch=73, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=70, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=75, pitch=72, start=4.875, end=5.25),  # G# (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=71, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=75, pitch=74, start=5.625, end=6.0),  # A (Approach)
]

bass.notes.extend(bass_notes)

# Piano: Diane
# 7th chords, comp on 2 and 4, stays out of the way but keeps the rhythm moving

piano_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F7: F, A, C, E (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
]

piano.notes.extend(piano_notes)

# Sax: Dante
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G#, B, G — a question, not a statement
# Start with F on 1, G# on 2, B on 3, G on 4
# Then space. Leave it open, don’t resolve.

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # G#
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0),  # G
    # Rest for the next two bars, let the silence speak
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
