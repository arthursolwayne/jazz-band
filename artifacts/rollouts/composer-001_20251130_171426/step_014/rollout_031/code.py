
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
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
# Dm7 chord: D F A C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in [1.5, 3.0, 4.5]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375))  # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 1.125))  # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.5, end=bar + 1.875))  # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 2.25, end=bar + 2.625))  # Snare on 4
    for i in range(4):
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar + i * 0.375, end=bar + i * 0.375 + 0.1875))  # Hihat on every eighth

drums.notes.extend(drum_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - A - D (Dm7) with some angularity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
