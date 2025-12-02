
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    # Bar 3 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    # Bar 4 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.1875)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.1875, end=start_time + 0.375)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.375, end=start_time + 0.5625)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.5625, end=start_time + 0.75)
    hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 0.9375)
    hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.9375, end=start_time + 1.125)
    hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.3125)
    hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.3125, end=start_time + 1.5)
    dr = [kick1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8]
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    dr.append(kick3)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    dr.append(snare4)
    return dr

drum_notes_bars2_4 = []
for i in range(3):
    start_time = 1.5 + i * 1.5
    drum_notes_bars2_4.extend(add_drums(start_time))
drums.notes.extend(drum_notes_bars2_4)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
