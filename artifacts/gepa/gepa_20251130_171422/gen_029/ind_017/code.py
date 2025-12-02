
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define key (D major)
key = 'D'

# Set up instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI drum kits use program 0
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Define note durations and timing
note_duration = 0.375  # 1 beat at 160 BPM is 0.375 seconds
bar_duration = 1.5  # 4 bars = 6 seconds, so 1.5 seconds per bar

# Bar 1: Little Ray on drums — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# MIDI note numbers: Kick = 36, Snare = 38, Hihat = 42
bar1_start = 0.0

# Kick on 1 and 3
drums.notes.append(Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + note_duration))
drums.notes.append(Note(velocity=100, pitch=36, start=bar1_start + 2 * note_duration, end=bar1_start + 3 * note_duration))

# Snare on 2 and 4
drums.notes.append(Note(velocity=100, pitch=38, start=bar1_start + note_duration, end=bar1_start + 2 * note_duration))
drums.notes.append(Note(velocity=100, pitch=38, start=bar1_start + 3 * note_duration, end=bar1_start + 4 * note_duration))

# Hihat on every eighth
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start, end=bar1_start + note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + note_duration / 2, end=bar1_start + note_duration))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + note_duration, end=bar1_start + 3 * note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + 3 * note_duration / 2, end=bar1_start + 2 * note_duration))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + 2 * note_duration, end=bar1_start + 5 * note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + 5 * note_duration / 2, end=bar1_start + 3 * note_duration))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + 3 * note_duration, end=bar1_start + 7 * note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar1_start + 7 * note_duration / 2, end=bar1_start + 4 * note_duration))

# Bar 2: Bass enters — walking line, chromatic approaches
# D major scale: D (2), E (4), F# (6), G (7), A (9), B (11), C# (13)
# Walking bass line in D major, chromatic approach on the 3rd (F#)
bar2_start = bar1_start + bar_duration

# D -> C# -> D -> E (walking line with chromatic approach)
bass.notes.append(Note(velocity=100, pitch=74, start=bar2_start, end=bar2_start + note_duration))  # D (2)
bass.notes.append(Note(velocity=100, pitch=73, start=bar2_start + note_duration, end=bar2_start + 2 * note_duration))  # C#
bass.notes.append(Note(velocity=100, pitch=74, start=bar2_start + 2 * note_duration, end=bar2_start + 3 * note_duration))  # D
bass.notes.append(Note(velocity=100, pitch=76, start=bar2_start + 3 * note_duration, end=bar2_start + 4 * note_duration))  # E

# Bar 2: Piano enters with 7th chords on 2 and 4
# D7 chord: D (2), F# (6), A (9), C (12)
bar2_piano_start = bar2_start

# D7 on 2 and 4
# 2nd beat: D7
piano.notes.append(Note(velocity=90, pitch=74, start=bar2_piano_start + note_duration, end=bar2_piano_start + 2 * note_duration))  # D
piano.notes.append(Note(velocity=90, pitch=76, start=bar2_piano_start + note_duration, end=bar2_piano_start + 2 * note_duration))  # F#
piano.notes.append(Note(velocity=90, pitch=79, start=bar2_piano_start + note_duration, end=bar2_piano_start + 2 * note_duration))  # A
piano.notes.append(Note(velocity=90, pitch=72, start=bar2_piano_start + note_duration, end=bar2_piano_start + 2 * note_duration))  # C

# 4th beat: D7 again
piano.notes.append(Note(velocity=90, pitch=74, start=bar2_piano_start + 3 * note_duration, end=bar2_piano_start + 4 * note_duration))  # D
piano.notes.append(Note(velocity=90, pitch=76, start=bar2_piano_start + 3 * note_duration, end=bar2_piano_start + 4 * note_duration))  # F#
piano.notes.append(Note(velocity=90, pitch=79, start=bar2_piano_start + 3 * note_duration, end=bar2_piano_start + 4 * note_duration))  # A
piano.notes.append(Note(velocity=90, pitch=72, start=bar2_piano_start + 3 * note_duration, end=bar2_piano_start + 4 * note_duration))  # C

# Bar 3: Sax enters with a sparse melody — a single motif, unresolved
bar3_start = bar2_start + bar_duration

# Tenor sax melody: D -> C# -> D -> E (same as bass, but with more space)
sax.notes.append(Note(velocity=110, pitch=74, start=bar3_start, end=bar3_start + note_duration))  # D
sax.notes.append(Note(velocity=110, pitch=73, start=bar3_start + note_duration, end=bar3_start + 2 * note_duration))  # C#
sax.notes.append(Note(velocity=110, pitch=74, start=bar3_start + 2 * note_duration, end=bar3_start + 3 * note_duration))  # D
sax.notes.append(Note(velocity=110, pitch=76, start=bar3_start + 3 * note_duration, end=bar3_start + 4 * note_duration))  # E

# Bar 4: Everyone plays in, sax continues melody, bass walks, piano continues 7th chords
bar4_start = bar3_start + bar_duration

# Bass continues walking pattern
bass.notes.append(Note(velocity=100, pitch=77, start=bar4_start, end=bar4_start + note_duration))  # F#
bass.notes.append(Note(velocity=100, pitch=79, start=bar4_start + note_duration, end=bar4_start + 2 * note_duration))  # G
bass.notes.append(Note(velocity=100, pitch=81, start=bar4_start + 2 * note_duration, end=bar4_start + 3 * note_duration))  # A
bass.notes.append(Note(velocity=100, pitch=84, start=bar4_start + 3 * note_duration, end=bar4_start + 4 * note_duration))  # B

# Piano continues with D7 on 2 and 4
# 2nd beat: D7
piano.notes.append(Note(velocity=90, pitch=74, start=bar4_start + note_duration, end=bar4_start + 2 * note_duration))  # D
piano.notes.append(Note(velocity=90, pitch=76, start=bar4_start + note_duration, end=bar4_start + 2 * note_duration))  # F#
piano.notes.append(Note(velocity=90, pitch=79, start=bar4_start + note_duration, end=bar4_start + 2 * note_duration))  # A
piano.notes.append(Note(velocity=90, pitch=72, start=bar4_start + note_duration, end=bar4_start + 2 * note_duration))  # C

# 4th beat: D7 again
piano.notes.append(Note(velocity=90, pitch=74, start=bar4_start + 3 * note_duration, end=bar4_start + 4 * note_duration))  # D
piano.notes.append(Note(velocity=90, pitch=76, start=bar4_start + 3 * note_duration, end=bar4_start + 4 * note_duration))  # F#
piano.notes.append(Note(velocity=90, pitch=79, start=bar4_start + 3 * note_duration, end=bar4_start + 4 * note_duration))  # A
piano.notes.append(Note(velocity=90, pitch=72, start=bar4_start + 3 * note_duration, end=bar4_start + 4 * note_duration))  # C

# Drums continue with same pattern
drums.notes.append(Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + note_duration))
drums.notes.append(Note(velocity=100, pitch=36, start=bar4_start + 2 * note_duration, end=bar4_start + 3 * note_duration))
drums.notes.append(Note(velocity=100, pitch=38, start=bar4_start + note_duration, end=bar4_start + 2 * note_duration))
drums.notes.append(Note(velocity=100, pitch=38, start=bar4_start + 3 * note_duration, end=bar4_start + 4 * note_duration))

# Hihat on every eighth
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start, end=bar4_start + note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + note_duration / 2, end=bar4_start + note_duration))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + note_duration, end=bar4_start + 3 * note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + 3 * note_duration / 2, end=bar4_start + 2 * note_duration))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + 2 * note_duration, end=bar4_start + 5 * note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + 5 * note_duration / 2, end=bar4_start + 3 * note_duration))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + 3 * note_duration, end=bar4_start + 7 * note_duration / 2))
drums.notes.append(Note(velocity=90, pitch=42, start=bar4_start + 7 * note_duration / 2, end=bar4_start + 4 * note_duration))

# Save the MIDI file
midi.write('jazz_intro_d_major.mid')
