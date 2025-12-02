
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for note in [(36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375), (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875)]:
        midi_note = pretty_midi.Note(velocity=100, pitch=note[0], start=bar * 1.5 + note[1], end=bar * 1.5 + note[1] + 0.125)
        drums.notes.append(midi_note)
    # Kick on 1
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5, end=bar * 1.5 + 0.125)
    drums.notes.append(midi_note)
    # Kick on 3
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5 + 0.75, end=bar * 1.5 + 0.875)
    drums.notes.append(midi_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Fm7 -> Bb7 -> Eb7 -> Am7
# Bar 2: Fm7 (F, Ab, C, D)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0)
piano.notes.append(note)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
note = pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.5)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=2.75, end=3.0)
bass.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.75)
sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane on piano: Bb7 (Bb, D, F, Ab)
note = pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5)
piano.notes.append(note)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5)
bass.notes.append(note)

# Dante on sax: Continue motif
note = pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)
sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane on piano: Eb7 (Eb, G, Bb, Db)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)
piano.notes.append(note)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)
bass.notes.append(note)

# Dante on sax: Finish motif
note = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0)
sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for note in [(36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375), (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875)]:
        midi_note = pretty_midi.Note(velocity=100, pitch=note[0], start=bar * 1.5 + note[1], end=bar * 1.5 + note[1] + 0.125)
        drums.notes.append(midi_note)
    # Kick on 1
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5, end=bar * 1.5 + 0.125)
    drums.notes.append(midi_note)
    # Kick on 3
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5 + 0.75, end=bar * 1.5 + 0.875)
    drums.notes.append(midi_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
