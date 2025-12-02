
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# DRUMS: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)
    
    drums.notes.extend([kick1, snare2, kick3, snare4, hihat])

# BASS: Walking line, chromatic approaches
bass_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # D minor walking bass line
    # D - Eb - F - G - A - Bb - B - C
    # Adjust as needed for chromatic movement
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.375))  # D
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=63, start=bar_start + 0.375, end=bar_start + 0.75))  # Eb
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.75, end=bar_start + 1.125))  # F
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 1.125, end=bar_start + 1.5))  # G

bass.notes.extend(bass_notes)

# PIANO: 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # D7 chord: D, F#, A, C
    if bar % 2 == 0:
        # Comp on beat 2
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 0.375, end=bar_start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 0.375, end=bar_start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 0.375, end=bar_start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.375, end=bar_start + 0.75))
    else:
        # Comp on beat 4
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 1.125, end=bar_start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.125, end=bar_start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 1.125, end=bar_start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 1.125, end=bar_start + 1.5))

piano.notes.extend(piano_notes)

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Bar 2
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75))  # A
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0))  # B
# Bar 3
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25))  # A
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5))  # G
# Bar 4
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75))  # A
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0))  # B
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25))  # A
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5))  # G

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
