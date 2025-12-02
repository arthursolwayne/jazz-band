
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define key: F minor (F, Gb, Ab, Bb, B, C, Db)
# We’ll use Fm7 as the tonal center for this intro

# --- Drums: Little Ray ---
# Create a drum instrument
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = Instrument(program=drums_program, is_drum=True)

# Kick on 1 and 3
kick_notes = [Note(36, 1.0, 0.0), Note(36, 1.0, 1.5)]  # Bar 1, kick on 1
kick_notes += [Note(36, 1.0, 3.0), Note(36, 1.0, 4.5)]  # Bar 2, kick on 1
kick_notes += [Note(36, 1.0, 6.0), Note(36, 1.0, 7.5)]  # Bar 3, kick on 1
kick_notes += [Note(36, 1.0, 9.0), Note(36, 1.0, 10.5)]  # Bar 4, kick on 1

# Snare on 2 and 4
snare_notes = [Note(38, 1.0, 0.75), Note(38, 1.0, 2.25)]  # Bar 1, snare on 2
snare_notes += [Note(38, 1.0, 3.75), Note(38, 1.0, 5.25)]  # Bar 2, snare on 2
snare_notes += [Note(38, 1.0, 6.75), Note(38, 1.0, 8.25)]  # Bar 3, snare on 2
snare_notes += [Note(38, 1.0, 9.75), Note(38, 1.0, 11.25)]  # Bar 4, snare on 2

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 12, 0.375):  # 12 seconds total, 0.375s per beat, 32 notes
    if i % 0.75 == 0:
        hihat_notes.append(Note(42, 0.125, i))

# Add all drum notes
drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)
pm.instruments.append(drums)

# --- Bass: Marcus ---
# Walking line in Fm, chromatic approaches, no repeated notes
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = Instrument(program=bass_program)

bass_notes = []

# Bar 1: F - Gb - Ab - Bb (Fm7)
bass_notes.append(Note(45, 1.0, 0.0))  # F
bass_notes.append(Note(46, 1.0, 0.75))  # Gb
bass_notes.append(Note(47, 1.0, 1.5))   # Ab
bass_notes.append(Note(48, 1.0, 2.25))  # Bb

# Bar 2: Bb - C - Db - F (chromatic approach)
bass_notes.append(Note(48, 1.0, 3.0))   # Bb
bass_notes.append(Note(49, 1.0, 3.75))  # C
bass_notes.append(Note(50, 1.0, 4.5))   # Db
bass_notes.append(Note(45, 1.0, 5.25))  # F

# Bar 3: F - Gb - Ab - Bb
bass_notes.append(Note(45, 1.0, 6.0))   # F
bass_notes.append(Note(46, 1.0, 6.75))  # Gb
bass_notes.append(Note(47, 1.0, 7.5))   # Ab
bass_notes.append(Note(48, 1.0, 8.25))  # Bb

# Bar 4: Bb - C - Db - F
bass_notes.append(Note(48, 1.0, 9.0))   # Bb
bass_notes.append(Note(49, 1.0, 9.75))  # C
bass_notes.append(Note(50, 1.0, 10.5))  # Db
bass_notes.append(Note(45, 1.0, 11.25)) # F

bass.notes.extend(bass_notes)
pm.instruments.append(bass)

# --- Piano: Diane ---
# Comp on 2 and 4 with 7th chords
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = Instrument(program=piano_program)

# Fm7 = F, Ab, Bb, C
# Bm7 = B, D, E, F#
# Ab7 = Ab, C, Eb, Gb
# Cm7 = C, Eb, F, G

# Bar 1: Rest on 1, Fm7 on 2
piano.notes.append(Note(64, 1.0, 0.75))   # F
piano.notes.append(Note(69, 1.0, 0.75))   # Ab
piano.notes.append(Note(71, 1.0, 0.75))   # Bb
piano.notes.append(Note(67, 1.0, 0.75))   # C

# Bar 2: Rest on 1, Bm7 on 2
piano.notes.append(Note(67, 1.0, 3.75))   # B
piano.notes.append(Note(72, 1.0, 3.75))   # D
piano.notes.append(Note(74, 1.0, 3.75))   # E
piano.notes.append(Note(68, 1.0, 3.75))   # F#

# Bar 3: Rest on 1, Ab7 on 2
piano.notes.append(Note(69, 1.0, 6.75))   # Ab
piano.notes.append(Note(74, 1.0, 6.75))   # C
piano.notes.append(Note(76, 1.0, 6.75))   # Eb
piano.notes.append(Note(67, 1.0, 6.75))   # Gb

# Bar 4: Rest on 1, Cm7 on 2
piano.notes.append(Note(67, 1.0, 9.75))   # C
piano.notes.append(Note(72, 1.0, 9.75))   # Eb
piano.notes.append(Note(74, 1.0, 9.75))   # F
piano.notes.append(Note(76, 1.0, 9.75))   # G

pm.instruments.append(piano)

# --- Tenor Sax: You ---
# Fm7 motif, short, singing, leaves it hanging
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = Instrument(program=sax_program)

# Bar 1: Little Ray alone, sax rests
# Bar 2: Start motif
# F (Ab), Bb (B), F (Ab), Bb (B) — Fm scale, ascending but chromatic

# Bar 2: Start of motif
note1 = Note(68, 0.8, 3.0)  # F (Ab)
note2 = Note(71, 0.8, 3.375) # Bb (B)
note3 = Note(68, 0.8, 4.125) # F (Ab)
note4 = Note(71, 0.8, 4.5)  # Bb (B)

# Bar 3: Leave it hanging — rest
# Bar 4: Return and finish
note5 = Note(68, 0.8, 6.0)  # F (Ab)
note6 = Note(71, 0.8, 6.375) # Bb (B)

sax.notes.extend([note1, note2, note3, note4, note5, note6])
pm.instruments.append(sax)

# Save the MIDI file
pm.write('f_minor_intro.mid')
