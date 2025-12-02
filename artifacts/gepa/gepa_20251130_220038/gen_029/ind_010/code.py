
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875), # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.375), # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.875), # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, snare1, hihat, kick2, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
