
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Initialize instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define note values (in seconds)
beat = 0.375  # 160 BPM = 60/160 = 0.375 seconds per beat
bar = 4 * beat  # 1.5 seconds per bar

# Drums: kick=36, snare=38, hihat=42
# Bar 1: Little Ray alone (0.0 - 1.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=beat))       # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=beat))       # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat, end=2*beat))    # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=beat, end=2*beat))    # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2*beat, end=3*beat))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2*beat, end=3*beat))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3*beat, end=4*beat))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3*beat, end=4*beat))  # Hihat on 4

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar, end=bar + beat))     # D (root)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=bar + beat, end=bar + 2*beat))  # Eb (chromatic)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar + 2*beat, end=bar + 3*beat))  # C (b7)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 3*beat, end=bar + 4*beat))  # D (root)

# Piano: 7th chords on 2 and 4, comp in Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + beat, end=bar + 2*beat))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + beat, end=bar + 2*beat))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar + beat, end=bar + 2*beat))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar + beat, end=bar + 2*beat))  # D (7th)

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 3*beat, end=bar + 4*beat))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 3*beat, end=bar + 4*beat))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar + 3*beat, end=bar + 4*beat))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar + 3*beat, end=bar + 4*beat))  # D (7th)

# Sax: Your moment. One short motif, sing it, leave it hanging.
# Start with a D minor motif, play it, then leave it open
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar, end=bar + 0.75*beat))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar + beat, end=bar + 1.5*beat))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar + 2*beat, end=bar + 2.5*beat))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar + 3*beat, end=bar + 3.5*beat))  # D (resolve)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Dm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 4*beat, end=bar + 5*beat))     # D (root)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=bar + 5*beat, end=bar + 6*beat))    # Eb (chromatic)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar + 6*beat, end=bar + 7*beat))    # C (b7)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 7*beat, end=bar + 8*beat))    # D (root)

# Piano: 7th chords on 2 and 4, comp in Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 5*beat, end=bar + 6*beat))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 5*beat, end=bar + 6*beat))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar + 5*beat, end=bar + 6*beat))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar + 5*beat, end=bar + 6*beat))  # D (7th)

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 7*beat, end=bar + 8*beat))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 7*beat, end=bar + 8*beat))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar + 7*beat, end=bar + 8*beat))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar + 7*beat, end=bar + 8*beat))  # D (7th)

# Drums: Same pattern in bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 4*beat, end=bar + 5*beat))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 4*beat, end=bar + 5*beat))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 5*beat, end=bar + 6*beat))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 5*beat, end=bar + 6*beat))  # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 6*beat, end=bar + 7*beat))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 6*beat, end=bar + 7*beat))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 7*beat, end=bar + 8*beat))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 7*beat, end=bar + 8*beat))  # Hihat on 4

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: End with a D to resolve back
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 8*beat, end=bar + 9*beat))  # D

# Piano: End on Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 8*beat, end=bar + 9*beat))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 8*beat, end=bar + 9*beat))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar + 8*beat, end=bar + 9*beat))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar + 8*beat, end=bar + 9*beat))  # D (7th)

# Drums: Same pattern in bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 8*beat, end=bar + 9*beat))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 8*beat, end=bar + 9*beat))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 9*beat, end=bar + 10*beat))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 9*beat, end=bar + 10*beat))  # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 10*beat, end=bar + 11*beat))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 10*beat, end=bar + 11*beat))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 11*beat, end=bar + 12*beat))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + 11*beat, end=bar + 12*beat))  # Hihat on 4

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file to disk
midi.write("dante_intro.mid")
